# Plotly

## mode
        Code: fig.update_traces(mode=<VALUE>, selector=dict(type='scatter'))
        Type: flaglist string. Any combination of "lines", "markers", "text" joined with a "+" OR "none".
        Examples: "lines", "markers", "lines+markers", "lines+markers+text", "none"

        Determines the drawing mode for this scatter trace. If the provided `mode` includes "text" then the `text` elements appear at the coordinates.
        Otherwise, the `text` elements appear on hover. If there are less than 20 points and the trace is not stacked then the default is
        "lines+markers". Otherwise, "lines".

## color
        Code: fig.update_traces(marker_line_color=<VALUE>, selector=dict(type='scatter'))
        Type: color or array of colors

        Sets the marker.line color. It accepts either a specific color or an array of numbers that are mapped to the colorscale relative to the max  and minvalues of the array or relative to `marker.line.cmin` and `marker.line.cmax` if set.
        
        
## symbol
        Code: fig.update_traces(marker_symbol=<VALUE>, selector=dict(type='scatter'))
        Type: enumerated or array of enumerateds , one of ( "0" | "0" | "circle" | "100" | "100" | "circle-open" | "200" | "200" | "circle-dot" | "300" | "300" | "circle-open-dot" | "1" | "1" | "square" | "101" | "101" | "square-open" | "201" | "201" | "square-dot" | "301" | "301" | "square-open-dot" | "2" | "2" | "diamond" | "102" | "102" | "diamond-open" | "202" | "202" | "diamond-dot" | "302" | "302" | "diamond-open-dot" | "3" | "3" | "cross" | "103" | "103" | "cross-open" | "203" | "203" | "cross-dot" | "303" | "303" | "cross-open-dot" | "4" | "4" | "x" | "104" | "104" | "x-open" | "204" | "204" | "x-dot" | "304" | "304" | "x-open-dot" | "5" | "5" | "triangle-up" | "105" | "105" | "triangle-up-open" | "205" | "205" | "triangle-up-dot" | "305" | "305" | "triangle-up-open-dot" | "6" | "6" | "triangle-down" | "106" | "106" | "triangle-down-open" | "206" | "206" | "triangle-down-dot" | "306" | "306" | "triangle-down-open-dot" | "7" | "7" | "triangle-left" | "107" | "107" | "triangle-left-open" | "207" | "207" | "triangle-left-dot" | "307" | "307" | "triangle-left-open-dot" | "8" | "8" | "triangle-right" | "108" | "108" | "triangle-right-open" | "208" | "208" | "triangle-right-dot" | "308" | "308" | "triangle-right-open-dot" | "9" | "9" | "triangle-ne" | "109" | "109" | "triangle-ne-open" | "209" | "209" | "triangle-ne-dot" | "309" | "309" | "triangle-ne-open-dot" | "10" | "10" | "triangle-se" | "110" | "110" | "triangle-se-open" | "210" | "210" | "triangle-se-dot" | "310" | "310" | "triangle-se-open-dot" | "11" | "11" | "triangle-sw" | "111" | "111" | "triangle-sw-open" | "211" | "211" | "triangle-sw-dot" | "311" | "311" | "triangle-sw-open-dot" | "12" | "12" | "triangle-nw" | "112" | "112" | "triangle-nw-open" | "212" | "212" | "triangle-nw-dot" | "312" | "312" | "triangle-nw-open-dot" | "13" | "13" | "pentagon" | "113" | "113" | "pentagon-open" | "213" | "213" | "pentagon-dot" | "313" | "313" | "pentagon-open-dot" | "14" | "14" | "hexagon" | "114" | "114" | "hexagon-open" | "214" | "214" | "hexagon-dot" | "314" | "314" | "hexagon-open-dot" | "15" | "15" | "hexagon2" | "115" | "115" | "hexagon2-open" | "215" | "215" | "hexagon2-dot" | "315" | "315" | "hexagon2-open-dot" | "16" | "16" | "octagon" | "116" | "116" | "octagon-open" | "216" | "216" | "octagon-dot" | "316" | "316" | "octagon-open-dot" | "17" | "17" | "star" | "117" | "117" | "star-open" | "217" | "217" | "star-dot" | "317" | "317" | "star-open-dot" | "18" | "18" | "hexagram" | "118" | "118" | "hexagram-open" | "218" | "218" | "hexagram-dot" | "318" | "318" | "hexagram-open-dot" | "19" | "19" | "star-triangle-up" | "119" | "119" | "star-triangle-up-open" | "219" | "219" | "star-triangle-up-dot" | "319" | "319" | "star-triangle-up-open-dot" | "20" | "20" | "star-triangle-down" | "120" | "120" | "star-triangle-down-open" | "220" | "220" | "star-triangle-down-dot" | "320" | "320" | "star-triangle-down-open-dot" | "21" | "21" | "star-square" | "121" | "121" | "star-square-open" | "221" | "221" | "star-square-dot" | "321" | "321" | "star-square-open-dot" | "22" | "22" | "star-diamond" | "122" | "122" | "star-diamond-open" | "222" | "222" | "star-diamond-dot" | "322" | "322" | "star-diamond-open-dot" | "23" | "23" | "diamond-tall" | "123" | "123" | "diamond-tall-open" | "223" | "223" | "diamond-tall-dot" | "323" | "323" | "diamond-tall-open-dot" | "24" | "24" | "diamond-wide" | "124" | "124" | "diamond-wide-open" | "224" | "224" | "diamond-wide-dot" | "324" | "324" | "diamond-wide-open-dot" | "25" | "25" | "hourglass" | "125" | "125" | "hourglass-open" | "26" | "26" | "bowtie" | "126" | "126" | "bowtie-open" | "27" | "27" | "circle-cross" | "127" | "127" | "circle-cross-open" | "28" | "28" | "circle-x" | "128" | "128" | "circle-x-open" | "29" | "29" | "square-cross" | "129" | "129" | "square-cross-open" | "30" | "30" | "square-x" | "130" | "130" | "square-x-open" | "31" | "31" | "diamond-cross" | "131" | "131" | "diamond-cross-open" | "32" | "32" | "diamond-x" | "132" | "132" | "diamond-x-open" | "33" | "33" | "cross-thin" | "133" | "133" | "cross-thin-open" | "34" | "34" | "x-thin" | "134" | "134" | "x-thin-open" | "35" | "35" | "asterisk" | "135" | "135" | "asterisk-open" | "36" | "36" | "hash" | "136" | "136" | "hash-open" | "236" | "236" | "hash-dot" | "336" | "336" | "hash-open-dot" | "37" | "37" | "y-up" | "137" | "137" | "y-up-open" | "38" | "38" | "y-down" | "138" | "138" | "y-down-open" | "39" | "39" | "y-left" | "139" | "139" | "y-left-open" | "40" | "40" | "y-right" | "140" | "140" | "y-right-open" | "41" | "41" | "line-ew" | "141" | "141" | "line-ew-open" | "42" | "42" | "line-ns" | "142" | "142" | "line-ns-open" | "43" | "43" | "line-ne" | "143" | "143" | "line-ne-open" | "44" | "44" | "line-nw" | "144" | "144" | "line-nw-open" | "45" | "45" | "arrow-up" | "145" | "145" | "arrow-up-open" | "46" | "46" | "arrow-down" | "146" | "146" | "arrow-down-open" | "47" | "47" | "arrow-left" | "147" | "147" | "arrow-left-open" | "48" | "48" | "arrow-right" | "148" | "148" | "arrow-right-open" | "49" | "49" | "arrow-bar-up" | "149" | "149" | "arrow-bar-up-open" | "50" | "50" | "arrow-bar-down" | "150" | "150" | "arrow-bar-down-open" | "51" | "51" | "arrow-bar-left" | "151" | "151" | "arrow-bar-left-open" | "52" | "52" | "arrow-bar-right" | "152" | "152" | "arrow-bar-right-open" )
        Default: "circle"

        Sets the marker symbol type. Adding 100 is equivalent to appending "-open" to a symbol name. Adding 200 is equivalent to appending "-dot" to a symbol name. Adding 300 is equivalent to appending "-open-dot" or "dot-open" to a symbol name.

## Plotly Line Styles

         line
        Code: fig.update_traces(line=dict(...), selector=dict(type='scatter'))
        Type: dict containing one or more of the keys listed below.

            color
            Code: fig.update_traces(line_color=<VALUE>, selector=dict(type='scatter'))
            Type: color

            Sets the line color.
            dash
            Code: fig.update_traces(line_dash=<VALUE>, selector=dict(type='scatter'))
            Type: string
            Default: "solid"

            Sets the dash style of lines. Set to a dash type string ("solid", "dot", "dash", "longdash", "dashdot", or "longdashdot") 
            or a dash length list in px (eg "5px,10px,2px,2px").


# Line Styles

    <option value="hex">6-pt stars</option>
    <option value="asterisk">asterisks</option>
    <option value="circle">circles</option>
    <option value="cross">crosses</option>
    <option value="dash">dashed</option>
    <option value="dot">dotted</option>
    <option value="fill">fill</option>
    <option value="plus">pluses</option>
    <option value="point">points</option>
    <option value="line" selected="selected">solid</option>
    <option value="trid">triangles (down)</option>
    <option value="tril">triangles (left)</option>
    <option value="trir">triangles (right)</option>
    <option value="triu">triangles (up)</option></select>

# Colors

    <option value="b">blue</option>
    <option value="c">cyan</option>
    <option value="dkb">dark blue</option>
    <option value="dkg">dark green</option>
    <option value="dkr">dark_red</option>
    <option value="g10">gray 10</option>
    <option value="g20">gray 20</option>
    <option value="g30">gray 30</option>
    <option value="g40">gray 40</option>
    <option value="g50">gray 50</option>
    <option value="g60">gray 60</option>
    <option value="g70">gray 70</option>
    <option value="g80">gray 80</option>
    <option value="g90">gray 90</option>
    <option value="g">green</option>
    <option value="ltb">light blue</option>
    <option value="ltg">light green</option>
    <option value="ltr">light red</option>
    <option value="m">magenta</option>
    <option value="r">red</option>
    <option value="w">white</option>
    <option value="y">yellow</option></select>
    
# limit_experiment">Experiment</label>
      <option value="CDEX-10">CDEX-10</option>
      <option value="CDMS I (SUF)">CDMS I (SUF)</option>
      <option value="CDMS II (Soudan)">CDMS II (Soudan)</option>
      <option value="CoGeNT">CoGeNT</option>
      <option value="COSME">COSME</option>
      <option value="COUPP">COUPP</option>
      <option value="CRESST">CRESST</option>
      <option value="Cuore">Cuore</option>
      <option value="CUORICINO">CUORICINO</option>
      <option value="DAMA">DAMA</option>
      <option value="DAMA Xe">DAMA Xe</option>
      <option value="DAMA/LIBRA">DAMA/LIBRA</option>
      <option value="DAMIC">DAMIC</option>
      <option value="DarkSide">DarkSide</option>
      <option value="DEAP CLEAN">DEAP CLEAN</option>
      <option value="DEAP-3600">DEAP-3600</option>
      <option value="DMTPC">DMTPC</option>
      <option value="DRIFT">DRIFT</option>
      <option value="Edelweiss">Edelweiss</option>
      <option value="ELEGANT V">ELEGANT V</option>
      <option value="EURECA">EURECA</option>
      <option value="Fermi">Fermi</option>
      <option value="GAMBIT">GAMBIT</option>
      <option value="GEDEON">GEDEON</option>
      <option value="Genino">Genino</option>
      <option value="Genius">Genius</option>
      <option value="Heidelberg">Heidelberg</option>
      <option value="Heidelberg-Moscow">Heidelberg-Moscow</option>
      <option value="IceCube">IceCube</option>
      <option value="IGEX">IGEX</option>
      <option value="KIMS">KIMS</option>
      <option value="KIMS DMRC">KIMS DMRC</option>
      <option value="LHC">LHC</option>
      <option value="LUX">LUX</option>
      <option value="LUX-ZEPLIN">LUX-ZEPLIN</option>
      <option value="MIBETA">MIBETA</option>
      <option value="Modane NaI">Modane NaI</option>
      <option value="NAIAD">NAIAD</option>
      <option value="NEWS-G">NEWS-G</option>
      <option value="PandaX">PandaX</option>
      <option value="PICASSO">PICASSO</option>
      <option value="PICO">PICO</option>
      <option value="ROSEBUD">ROSEBUD</option>
      <option value="Saclay">Saclay</option>
      <option value="SIMPLE">SIMPLE</option>
      <option value="SuperCDMS">SuperCDMS</option>
      <option value="SuperK">SuperK</option>
      <option value="TEXONO">TEXONO</option>
      <option value="Theory">Theory</option>
      <option value="TOKYO">TOKYO</option>
      <option value="UKDMC">UKDMC</option>
      <option value="WARP">WARP</option>
      <option value="XENON10">XENON10</option>
      <option value="XENON100">XENON100</option>
      <option value="XENON1T">XENON1T</option>
      <option value="XENONnT">XENONnT</option>
      <option value="XMASS">XMASS</option>
      <option value="ZEPLIN I">ZEPLIN I</option>
      <option value="ZEPLIN II">ZEPLIN II</option>
      <option value="ZEPLIN III">ZEPLIN III</option>
      <option value="ZEPLIN IV">ZEPLIN IV</option></select></p>
  
# Year
      <option value="" selected="selected"></option>
      <option value="1980">1980</option>
      <option value="1981">1981</option>
      <option value="1982">1982</option>
      <option value="1983">1983</option>
      <option value="1984">1984</option>
      <option value="1985">1985</option>
      <option value="1986">1986</option>
      <option value="1987">1987</option>
      <option value="1988">1988</option>
      <option value="1989">1989</option>
      <option value="1990">1990</option>
      <option value="1991">1991</option>
      <option value="1992">1992</option>
      <option value="1993">1993</option>
      <option value="1994">1994</option>
      <option value="1995">1995</option>
      <option value="1996">1996</option>
      <option value="1997">1997</option>
      <option value="1998">1998</option>
      <option value="1999">1999</option>
      <option value="2000">2000</option>
      <option value="2001">2001</option>
      <option value="2002">2002</option>
      <option value="2003">2003</option>
      <option value="2004">2004</option>
      <option value="2005">2005</option>
      <option value="2006">2006</option>
      <option value="2007">2007</option>
      <option value="2008">2008</option>
      <option value="2009">2009</option>
      <option value="2010">2010</option>
      <option value="2011">2011</option>
      <option value="2012">2012</option>
      <option value="2013">2013</option>
      <option value="2014">2014</option>
      <option value="2015">2015</option>
      <option value="2016">2016</option>
      <option value="2017">2017</option>
      <option value="2018">2018</option>
      <option value="2019">2019</option>
      <option value="2020">2020</option>
      <option value="2021">2021</option>
      <option value="2022">2022</option>
      
# Result Type

    result_type_" multiple="multiple" name="limits_search[result_type][]" size="6"><option value="all" selected="selected">All</option>
    <option value="Exp">Experiment</option>
    <option value="Proj">Projection</option>
    <option value="Th">Theory</option>
    <option value="Other">Other</option>
    <option value="Personal">Personal</option></select></td>

# Spin Type

    <option value="N">neither</option>
    <option value="SD">spin-dependent</option>
    <option value="SI">spin-independent</option></select></td>
    
   
