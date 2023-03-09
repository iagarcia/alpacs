inotifywait -m ./health/inbound -e create -e moved_to |
    while read directory action file; do
        if [[ "$file" =~ .*dcm$ ]]; then # Does the file end with .xml?
            echo "dcm file" # If so, do your thing here!
	    mv ./health/inbound/$file /home/admin/AWS_S3/
        fi
    done
