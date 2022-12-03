#!/bin/bash

# HOW TO USE ?
# aoc : (with no args) return today's problem in a new dir with input.txt, if problem isn't up return error
# aoc -g 1 2021: year and day, if problem isn't up return error
# aoc -s part answer : submit the answer for today's problem
# aoc -s answer -y 2021 -d 5 : submit the answer for that date


# the session max age lasts for years lol, mine expires at 2032 LOL
# login on the browser and get the session id from the local storage of the browser.
SESSION="YOUR SESSION HERE"
USER_AGENT="User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"

YEAR=`date +%Y`
DAY=`date +%d`

check_online () {
    YEAR="${2:-`date +%Y`}"
    DAY="${1:-`date +%d`}"
    URL="https://adventofcode.com/$YEAR/day/$DAY"

    echo "Checking the problem for that day: ${YEAR}/${DAY}"

    AOC_ONLINE=$(curl --write-out '%{http_code}' --silent --output /dev/null $URL)
    if [[ $AOC_ONLINE == 404 ]]; then
        echo "Advent of code isn't available for this day." && exit 1
    fi       
    echo "Found here : $URL"
}

get_input () {
    # download the input
    YEAR="${2:-`date +%Y`}"
    DAY="${1:-`date +%d`}"
    curl "https://adventofcode.com/$YEAR/day/$DAY/input" -H "${USER_AGENT}" \
        -H "Cookie: session=${SESSION}" > "$YEAR/day$DAY/input.txt"
}

get_problem() {
    # get the problem into markdown format, contains part1&2
    YEAR="${2:-`date +%Y`}"
    DAY="${1:-`date +%d`}"
    curl "https://adventofcode.com/$YEAR/day/$DAY" -H "${USER_AGENT}" \
        -H "Cookie: session=${SESSION}" | pandoc --from html --to markdown_strict -o "$YEAR/day$1/problem.md"
}
automate_problem () {
    mkdir -vp "$2/day$1" >/dev/null 2>&1
    get_problem $1 $2
    get_input $1 $2
}

submit_answer () {
    curl "https://adventofcode.com/$YEAR/day/$DAY/answer" -X \
        POST -H "${USER_AGENT}"  \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -H "Cookie: session=${SESSION}" \
        --data-raw "level=$1&answer=$2"
}

while [[ $# -ge 0 ]]; do
    key=$1
    shift
    case "$key" in
        -g | --get) 
            check_online $1 $2
            automate_problem $1 $2
            break
            ;;
        -c | --check) 
            check_online $1 $2
            break
            ;;
        -s | --submit) 
            # TODO: submit only works for today's unlocked problem.
            submit_answer $1 $2
            break
            ;;
        *) 
            check_online
            automate_problem
            break
        ;;
    esac
done
