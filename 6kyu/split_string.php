<?php
// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001


function solution($str)
{
    if ($str == '') return [];
    if (strlen($str) % 2 != 0) $str .= '_';
    return str_split($str, 2);
}

echo ["ab", "cd", "ef"] === solution("abcdef") ? 'true' : 'false';
echo "\n";
echo ["ab", "cd", "ef", "g_"] === solution("abcdefg") ? 'true' : 'false';
echo "\n";
echo [] === solution("") ? 'true' : 'false';
echo "\n";
