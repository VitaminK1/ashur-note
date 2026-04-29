param(
    [string]$Config = "properdocs.yml",
    [string]$BaselineDir = "C:\tmp\ashur-note-baseline",
    [string]$CandidateDir = "C:\tmp\ashur-note-candidate",
    [switch]$HtmlOnly,
    [switch]$BuildBaseline
)

$ErrorActionPreference = "Stop"

function Invoke-StrictBuild {
    param(
        [string]$OutputDir
    )

    & properdocs build --strict -f $Config -d $OutputDir
    if ($LASTEXITCODE -ne 0) {
        throw "properdocs build failed for $OutputDir."
    }
}

function Invoke-NodeCheck {
    param(
        [string]$Path
    )

    & node --check $Path
    if ($LASTEXITCODE -ne 0) {
        throw "node --check failed for $Path."
    }
}

function Get-SiteManifest {
    param(
        [string]$Root,
        [switch]$OnlyHtml
    )

    $files = Get-ChildItem -Path $Root -Recurse -File
    if ($OnlyHtml) {
        $files = $files | Where-Object { $_.Extension -eq ".html" }
    }

    $files |
        ForEach-Object {
            $relative = $_.FullName.Substring($Root.Length).TrimStart("\")
            $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
            [pscustomobject]@{
                Path = $relative
                Hash = $hash
            }
        } |
        Sort-Object Path
}

if ($BuildBaseline) {
    Invoke-StrictBuild -OutputDir $BaselineDir
}

Invoke-StrictBuild -OutputDir $CandidateDir

Invoke-NodeCheck -Path "docs\javascripts\collapsible.js"
Invoke-NodeCheck -Path "docs\javascripts\lore.js"

$baseline = Get-SiteManifest -Root $BaselineDir -OnlyHtml:$HtmlOnly
$candidate = Get-SiteManifest -Root $CandidateDir -OnlyHtml:$HtmlOnly
$diff = Compare-Object $baseline $candidate -Property Path, Hash

if ($diff) {
    $diff | Format-Table -AutoSize
    throw "Generated site differs from baseline."
}

if ($HtmlOnly) {
    "Generated HTML matches baseline."
} else {
    "Generated site matches baseline."
}
