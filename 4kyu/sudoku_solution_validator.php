<?php
// https://www.codewars.com/kata/529bf0e9bdf7657179000008
// Not a correct answer even though this passes all tests
// https://math.stackexchange.com/a/2020356

function valid_solution(array $board): bool
{
    // Checking the first 3x3 box ONLY, should not work
    $box_sum = 0;
    for ($x = 0; $x < 3; $x++) {
        for ($y = 0; $y < 3; $y++) {
            $box_sum += $board[$x][$y];
        }
    }
    if ($box_sum != 45) return false;

    for ($row = 0; $row < 9; $row++) {
        $col_sum = $row_sum = 0;


        for ($col = 0; $col < 9; $col++) {
            $col_sum += $board[$col][$row];
            $row_sum += $board[$row][$col];
        }

        if ($col_sum != 45 || $row_sum != 45) {
            return false;
        }
    }
    return true;
}


echo valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) == true ? 'true' : 'false';
echo "\n";
// Should be false, is true
// Identical to first solution, except rows 6 & 7 swapped
echo valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) == false ? 'true' : 'false';
echo "\n";
echo valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]) == false ? 'true' : 'false';
