#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DOCDIR="${DIR}/docu/"

COMMITMSG="Documentation updated, check diff."

git add $DOCDIR && git commit -m $COMMITMSG
