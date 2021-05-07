<?php
// https://www.codewars.com/kata/550f22f4d758534c1100025a


const OPPOSITE_OF = [
    'NORTH' => 'SOUTH',
    'SOUTH' => 'NORTH',
    'EAST' => 'WEST',
    'WEST' => 'EAST',
];


function dirReduc($arr)
{
    $simplified = array_reduce($arr, function ($carry, $direction) {
        if (OPPOSITE_OF[$direction] != end($carry)) {
            $carry[] = $direction;
        } else {
            array_pop($carry);
        }
        return $carry;
    }, []);
    return $simplified;
}


$a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"];
echo dirReduc($a) === ["WEST"] ? 'true' : 'false';
echo "\n";
$b = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"];
echo dirReduc($b) === [] ? 'true' : 'false';
echo "\n";
$c = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"];
echo dirReduc($c) === ["NORTH"] ? 'true' : 'false';
echo "\n";
