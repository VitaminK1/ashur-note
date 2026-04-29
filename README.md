# Ashur Note

본 문서는 에피드게임즈에서 개발한 트릭컬 리바이브에 등장하는 캐릭터, 에슈르(Ashur)에 관한 것을 기록하기 위한 목적으로 만들었습니다.
This document is for recording information about the character Ashur of Trickcal Re:vive, a mobile game developed by Epid Games.

This is a fan content.
Trickcal copyrighted by EPIDGames.

## Build

This project uses ProperDocs as the MkDocs-compatible site builder.

```bash
pip install -r requirements.txt
properdocs build --strict -f properdocs.yml
```

To serve locally:

```bash
properdocs serve -f properdocs.yml
```

For output-preserving refactors, see `MAINTENANCE.md` and run:

```powershell
tools\verify-site.ps1 -BuildBaseline
```
