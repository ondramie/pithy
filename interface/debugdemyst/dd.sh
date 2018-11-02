${@} 2> .tmp_file.error
if [ ! -z "$(cat .tmp_file.error)" ]
then
    cat .tmp_file.error
    echo
    echo "Search elasticsearch for:"
    searchvar=$(tail -n1 .tmp_file.error | perl -pe "s/'(.*?)'//g")
    echo "$searchvar"
    echo "The elasticsearch result is: "
    python3 ~/debugDemyst/upload/es_interface.py "$searchvar" > temp.txt
    html2text temp.txt
fi
