set key right top box

set xlabel "Distance"
set ylabel "Energy [arbitrary units]" 

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5
set style line 2 lc rgb '#2F4F4F' lt 1 lw 2 pt 7 ps 1.5
set style line 3 lc rgb '#8B0000' lt 1 lw 2 pt 7 ps 1.5
set style line 4 lc rgb '#006400' lt 1 lw 2 pt 7 ps 1.5
set style line 5 lc rgb '#FF1493' lt 1 lw 2 pt 7 ps 1.5
set style line 6 lc rgb '#FF4500' lt 1 lw 2 pt 7 ps 1.5
set style line 7 lc rgb '#CD5C5C' lt 1 lw 2 pt 7 ps 1.5
set style line 8 lc rgb '#696969' lt 1 lw 2 pt 7 ps 1.5

plot 'LJ_Plot_3' u 1:2 with lines ls 1 title "Extra Point at 3", \
     'LJ_Plot_4' u 1:2 with lines ls 2 title "Extra Point at 4", \
     'LJ_Plot_5' u 1:2 with lines ls 3 title "Extra Point at 5", 'LJ_Plot_6' u 1:2 with lines ls 4 title "Extra Point at 6", \
     'LJ_Plot_7' u 1:2 with lines ls 5 title "Extra Point at 7", \
     'LJ_Plot_8' u 1:2 with lines ls 6 title "Extra Point at 8", 'LennardJones.txt' u 1:2 with lines ls 8 title "Original"
