## Step-5: Build ml pipeline

Tasks:

1. install DVC (in a virtual environment)
2. automate ML pipeline with DVC
3. setup dependencies and outputs
4. setup parameters

Explore DVC repro:

- [ ]  run `dvc repro` (assume we do this for 1st time)
- [ ]  run `dvc repro` (no changes, DVC skips all stages)
- [ ]  run `dvc repro -f` (force running ML pipeline)
- [ ]  run `dvc repro train` (run only `train` stage from `dvc.yaml`)
- [ ]  update `train` stage configs and run `dvc repro`
- [ ]  update `src/stage/train.py` code and run `dvc repro`
- [ ]  remove `reports/metrics.json` and run `dvc repro`

**Requirements: for each stage, explicitly define dependencies (code and data)