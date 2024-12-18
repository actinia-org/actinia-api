Steps when releasing actinia-api:

## 0. Steps for major updates
* If the release is a major update, it needs to be prepared like described in the [WIKI](https://github.com/mundialis/actinia_core/wiki/Versioning).

## 1. Prepare release and version
* Run in terminal
    ```
    ESTIMATED_VERSION=3.0.1

    gh api repos/mundialis/actinia-api/releases/generate-notes -f tag_name="$ESTIMATED_VERSION" -f target_commitish=main -q .body
    ```
* Go to https://github.com/mundialis/actinia-api/releases/new
* Copy the output of terminal command to the release description
* Change heading `## What's Changed` to `### Changed`, `### Fixed`, `### Added` or what applicable and sort list amongst these headings.
* You can [compare manually](https://github.com/mundialis/actinia-api/compare/3.0.0...3.0.1) if all changes are included. If changes were pushed directly to main branch, they are not included.
* Check if `ESTIMATED_VERSION` increase still fits - we follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
* Fill in tag and release title with this version
* At the bottom of the release, add
  "generated with `gh api repos/mundialis/actinia-api/releases/generate-notes -f tag_name="$ESTIMATED_VERSION" -f target_commitish=main -q .body`" and replace `$ESTIMATED_VERSION` with the actual version.
* DO NOT click "save" yet!!

## 2. Update pyproject.toml
* In [pyproject.toml](https://github.com/mundialis/actinia-api/blob/main/pyproject.toml), update [version](https://github.com/mundialis/actinia-api/blob/main/CITATION.cff#L7) in main branch

## 3. Release
* Now you can save the release

## 4. Update actinia-api version in other repos
* [actinia-core dependencies](https://github.com/actinia-org/actinia-core/blob/main/pyproject.toml#L38)
* `ACTINIA_API_VERSION` in [actinia-docker](https://github.com/actinia-org/actinia-docker/blob/main/actinia-alpine/Dockerfile#L98)
