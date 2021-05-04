<?php
// https://www.codewars.com/kata/54e6533c92449cc251001667

function uniqueInOrder($iterable)
{
    $input = is_string($iterable) ? str_split($iterable)  : $iterable;
    $result = [];
    $prev = '';
    foreach ($input as $item) {
        if ($prev !== $item) {
            $result[] = $item;
        }
        $prev = $item;
    }
    return $result;
}

echo ['A', 'B', 'C', 'D', 'A', 'B'] === uniqueInOrder('AAAABBBCCDAABBB') ? 'true' : 'false';
