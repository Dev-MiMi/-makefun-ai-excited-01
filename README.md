# -makefun-ai-excited-01

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/Dev-MiMi/-makefun-ai-excited-01/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/Dev-MiMi/-makefun-ai-excited-01/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

**Unzip the Storm** captures a red-coated figure pulling open a storm-sky zipper to reveal a golden sun. A Node 22 program verifies the committed artwork and copies its exact bytes to the required image output.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Use a Node 22 distribution with native TypeScript support. For a Node build without it, the source also runs as a standard ES module from the repository root:

```sh
MAKEFUN_OUTPUT_DIR=out node --input-type=module < main.ts
```

The default destination is `/output/entry.png`. The file contains JPEG bytes, which the bounty accepts with this filename. Runtime uses only Node's standard library, without installation or network access. The program checks the artwork's SHA256 and size, verifies its copy, and renames a temporary file to publish a complete image.

## Artwork provenance

The user supplied `AI.png`, an image they generated outside the recorded build. Its generation session, tool and prompt were not provided or recorded. This is an input artwork asset, not transcript-authored code.

The original is 1254 × 1254 pixels and 2,896,862 bytes and was left intact. During the recorded build, Pillow resized the complete composition with Lanczos to 1024 × 1024, encoded an optimized JPEG at quality 98 with no chroma subsampling, and removed metadata. The committed asset, `assets/unzip-the-storm.jpg`, is 974,391 bytes. Full-size and 300-pixel views were inspected, and the asset completely decoded before packaging. No image-generation API was called during this build.

SHA256: `5bab9a3e253e4bdd6b56370927a13d4a3e7bca1862f2ec42a8a48a2b864843ad`.

The initial copier was authored in an earlier, interrupted recorded build session. The continuation retained its asset path, output selection and directory creation, then added integrity checks and atomic output publication. The earlier setup conversation authored no entry code. Private recording files are maintained outside this repository.

## License

MIT; see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=pjp61cd9&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards</sub>
