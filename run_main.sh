#!/bin/bash
export PYTHONPATH=$(pwd)

EXPERIMENT_NAME="yyyymmdd-test-experiment"
CLEARML_PROJECT_NAME="gah3605a-clearmlxhydra-test"
CLEARML_TASK_NAME="yyyymmdd-hydra-test"
BATCH_SIZE=64
EPOCH=10

python3 src/main.py experiment.name=${EXPERIMENT_NAME} \
                     clearml.project_name=${CLEARML_PROJECT_NAME} \
                     clearml.task_name=${CLEARML_TASK_NAME} \
                     train.batch_size=${BATCH_SIZE} \
                     train.epochs=${EPOCH}
