SCRIPT_DIR=./scripts

.PHONY: fetch
fetch_phishtank:
	sh ${SCRIPT_DIR}/fetch.sh

.PHONY: run
run:
	sh ${SCRIPT_DIR}/run.sh

.PHONY: all
all:
	sh ${SCRIPT_DIR}/fetch.sh
	sh ${SCRIPT_DIR}/run.sh