#!/bin/bash

file=logfile.txt


case $1 in
    start)
        tag=$( tail -n 1 $file )
        set - $tag
        if [ $1 = "LABEL" ]
        then
            echo -e "Must end active task.\nUse: $0 stop to end task."
        else 
            echo -e "START $(date)\nLABEL ${*:2}" >> $file  
        fi
        ;;


	stop)
        tag=$( tail -n 1 $file )
        set - $tag
        if ! [ $1 = "LABEL" ] 
        then
            echo -e "No active task.\nUse: $0 start [label] to start task."
        else
		    echo -e "END $(date)\n" >> $file
        fi
        ;;

	status)
        tag=$( tail -n 1 $file )
        set - $tag
        if [ $1 = "LABEL" ]
        then
            echo "Active task: ${*:2}"
        else
            echo "No active task."
        fi
		 ;;
    log) 
        if [[ ! -s $file ]]; then
            echo "Logfile is empty."   
        fi
            #Så lenge filen har en linje:
            while IFS= read -r line; do
            if [ "$line" != "" ]; then
                set - $line
                if [ $1 = "START" ]; then
                    startClockTime=$5

                elif [ $1 = "LABEL" ]; then
                    currentLabel="${*:2}"

                elif [ $1 = "END" ]; then
                    endClockTime=$5  
                    startSeconds=`date +%s -d "${startClockTime}"`
                    endSeconds=`date +%s -d "${endClockTime}"`
                    #Finner differansen mellom tidene.
                    diffSeconds=`expr ${endSeconds} - ${startSeconds}`
                    printTime=`date +%H:%M:%S -ud @${diffSeconds}`
                    echo "${currentLabel}: ${printTime}"
                else
                continue    
                fi
            fi
            done < $file

            #Hvis en task er aktiv.
            tag=$( tail -1 $file )
            set - $tag
            if [ $1 = "LABEL" ]; then
                nowClockTime=`date "+%T"`
                startSeconds=`date +%s -d "${startClockTime}"`
                nowSeconds=`date +%s -d "${nowClockTime}"`
                 #Finner differansen mellom tidene.
                diffSeconds=`expr ${nowSeconds} - ${startSeconds}`
                printTime=`date +%H:%M:%S -ud @${diffSeconds}`
                echo "${currentLabel}: ${printTime}"
            fi
        ;;
    *)  
        #Hvis bruker kjører programmet på feil måte.
        echo -e $"$1 is not a valid operator.\nUsage: $0 {start [label]|stop|status|log}" ;;
esac

