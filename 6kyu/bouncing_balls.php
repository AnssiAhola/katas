<?php
// https://www.codewars.com/kata/5544c7a5cb454edb3c000047

function bouncingBall($h, $bounce, $window)
{
    if (
        !($h > 0) ||
        !($bounce > 0 && $bounce < 1) ||
        !($window < $h)
    ) return -1;

    $ball_h = $h;
    $count = 0;
    while ($ball_h > $window) {
        // Coming down
        $count++;
        $ball_h *= $bounce;
        // Going up
        if ($ball_h > $window) $count++;
    }
    return $count;
}



echo bouncingBall(3.0, 0.66, 1.5) == 3 ? 'true' : 'false';
echo "\n";
echo bouncingBall(30.0, 0.66, 1.5) == 15 ? 'true' : 'false';
echo "\n";
echo bouncingBall(10, 0.6, 10) == -1 ? 'true' : 'false';
echo "\n";
