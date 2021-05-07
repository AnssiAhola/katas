<?php
// https://www.codewars.com/kata/52742f58faf5485cae000b9a


function addUnits($value, $unit)
{
    if ($value == 0) return null;
    $ret = "{$value} {$unit}";
    $ret .= $value == 1 ? '' : 's';
    return $ret;
}

function format_duration(int $seconds)
{
    if ($seconds == 0) return 'now';
    // Filter out nulls and join with ', '
    $result = join(', ', array_filter(
        [
            addUnits((int) ($seconds / 60 / 60 / 24 / 365), 'year'),
            addUnits((int) ($seconds / 60 / 60 / 24) % 365, 'day'),
            addUnits((int) ($seconds / 60 / 60) % 24, 'hour'),
            addUnits((int) ($seconds / 60) % 60, 'minute'),
            addUnits($seconds % 60, 'second')
        ]
    ));
    // Replace last ', ' with ' and'
    // https://stackoverflow.com/a/53640494
    return preg_replace("((.*),)", "$1 and", $result);
}


echo "1 second" == format_duration(1) ? 'true' : 'false';
echo "\n";
echo "1 minute and 2 seconds" == format_duration(62) ? 'true' : 'false';
echo "\n";
echo "2 minutes" == format_duration(120) ? 'true' : 'false';
echo "\n";
echo "1 hour" == format_duration(3600) ? 'true' : 'false';
echo "\n";
echo "1 hour, 1 minute and 2 seconds" == format_duration(3662) ? 'true' : 'false';
echo "\n";
