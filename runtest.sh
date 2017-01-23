coverage run --rcfile=.coveragerc --source . ./manage.py test $@

if [ ! "$@" ] ; then
    echo
    coverage report
fi

coverage html
coverage report
