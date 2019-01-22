#!/bin/bash -uex

# This script is expected to be called from Jenkins.
# The following environment variables expected to be set:
# - CUDA (CUDA verseion; 7.0, 7.5, etc. or sdist)
# - PYTHON (python version; 2.7.6, 3.6.0, etc.)
# This script also expects that `chainer` source tree exists in the same directory.

###
### Build & Verify Distribution
###

# Set DIST_OPTIONS and DIST_FILE_NAME
case ${CUDA} in
  sdist )
    DIST_OPTIONS="--target sdist --python ${PYTHON}"
    eval $(./get_dist_info.py --target sdist --source chainer)
    ;;
  * )
    DIST_OPTIONS="--target wheel-linux --python ${PYTHON} --cuda ${CUDA}"
    eval $(./get_dist_info.py --target wheel-linux --source chainer --cuda ${CUDA} --python ${PYTHON})
    ;;
esac

./dist.py --action build ${DIST_OPTIONS} --source chainer --output .

VERIFY_ARGS="--test release-tests/common --test release-tests/cudnn"

./dist.py --action verify ${DIST_OPTIONS} --dist ${DIST_FILE_NAME} ${VERIFY_ARGS}
