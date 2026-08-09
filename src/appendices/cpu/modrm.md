# ModR/M Reference

## 16-Bit ModR/M

<div class="table-wrapper">
<table class="modrm-table">
    <thead>
        <tr>
            <td colspan="5">r8</td>
            <td>AL</td>
            <td>CL</td>
            <td>DL</td>
            <td>BL</td>
            <td>AH</td>
            <td>CH</td>
            <td>DH</td>
            <td>BH</td>
        </tr>
        <tr>
            <td colspan="5">r16</td>
            <td>AX</td>
            <td>CX</td>
            <td>DX</td>
            <td>BX</td>
            <td>SP</td>
            <td>BP</td>
            <td>SI</td>
            <td>DI</td>
        </tr>
        <tr>
            <td colspan="5">Ext</td>
            <td>0</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
        </tr>
        <tr>
            <td colspan="5">REG</td>
            <td>000</td>
            <td>001</td>
            <td>010</td>
            <td>011</td>
            <td>100</td>
            <td>101</td>
            <td>110</td>
            <td>111</td>
        </tr>
        <tr class="section-start">
            <th aria-label="Addressing mode"></th>
            <th>Effective Address</th>
            <th>Base</th>
            <th>Mod</th>
            <th>R/M</th>
            <th colspan="8">Value of ModR/M Byte</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th class="addressing-mode" rowspan="24" scope="rowgroup"><span>Memory Addressing Modes</span></th>
            <td>[BX+SI]</td>
            <td>DS</td>
            <td rowspan="8">00</td>
            <td>000</td>
            <td>00</td>
            <td>08</td>
            <td>10</td>
            <td>18</td>
            <td>20</td>
            <td>28</td>
            <td>30</td>
            <td>38</td>
        </tr>
        <tr>
            <td>[BX+DI]</td>
            <td>DS</td>
            <td>001</td>
            <td>01</td>
            <td>09</td>
            <td>11</td>
            <td>19</td>
            <td>21</td>
            <td>29</td>
            <td>31</td>
            <td>39</td>
        </tr>
        <tr>
            <td>[BP+SI]</td>
            <td>SS</td>
            <td>010</td>
            <td>02</td>
            <td>0A</td>
            <td>12</td>
            <td>1A</td>
            <td>22</td>
            <td>2A</td>
            <td>32</td>
            <td>3A</td>
        </tr>
        <tr>
            <td>[BP+DI]</td>
            <td>SS</td>
            <td>011</td>
            <td>03</td>
            <td>0B</td>
            <td>13</td>
            <td>1B</td>
            <td>23</td>
            <td>2B</td>
            <td>33</td>
            <td>3B</td>
        </tr>
        <tr>
            <td>[SI]</td>
            <td>DS</td>
            <td>100</td>
            <td>04</td>
            <td>0C</td>
            <td>14</td>
            <td>1C</td>
            <td>24</td>
            <td>2C</td>
            <td>34</td>
            <td>3C</td>
        </tr>
        <tr>
            <td>[DI]</td>
            <td>DS</td>
            <td>101</td>
            <td>05</td>
            <td>0D</td>
            <td>15</td>
            <td>1D</td>
            <td>25</td>
            <td>2D</td>
            <td>35</td>
            <td>3D</td>
        </tr>
        <tr>
            <td>disp16</td>
            <td>DS</td>
            <td>110</td>
            <td>06</td>
            <td>0E</td>
            <td>16</td>
            <td>1E</td>
            <td>26</td>
            <td>2E</td>
            <td>36</td>
            <td>3E</td>
        </tr>
        <tr>
            <td>[BX]</td>
            <td>DS</td>
            <td>111</td>
            <td>07</td>
            <td>0F</td>
            <td>17</td>
            <td>1F</td>
            <td>27</td>
            <td>2F</td>
            <td>37</td>
            <td>3F</td>
        </tr>
        <tr class="section-start">
            <td>[BX+SI]+disp8</td>
            <td>DS</td>
            <td rowspan="8">01</td>
            <td>000</td>
            <td>40</td>
            <td>48</td>
            <td>50</td>
            <td>58</td>
            <td>60</td>
            <td>68</td>
            <td>70</td>
            <td>78</td>
        </tr>
        <tr>
            <td>[BX+DI]+disp8</td>
            <td>DS</td>
            <td>001</td>
            <td>41</td>
            <td>49</td>
            <td>51</td>
            <td>59</td>
            <td>61</td>
            <td>69</td>
            <td>71</td>
            <td>79</td>
        </tr>
        <tr>
            <td>[BP+SI]+disp8</td>
            <td>SS</td>
            <td>010</td>
            <td>42</td>
            <td>4A</td>
            <td>52</td>
            <td>5A</td>
            <td>62</td>
            <td>6A</td>
            <td>72</td>
            <td>7A</td>
        </tr>
        <tr>
            <td>[BP+DI]+disp8</td>
            <td>SS</td>
            <td>011</td>
            <td>43</td>
            <td>4B</td>
            <td>53</td>
            <td>5B</td>
            <td>63</td>
            <td>6B</td>
            <td>73</td>
            <td>7B</td>
        </tr>
        <tr>
            <td>[SI]+disp8</td>
            <td>DS</td>
            <td>100</td>
            <td>44</td>
            <td>4C</td>
            <td>54</td>
            <td>5C</td>
            <td>64</td>
            <td>6C</td>
            <td>74</td>
            <td>7C</td>
        </tr>
        <tr>
            <td>[DI]+disp8</td>
            <td>DS</td>
            <td>101</td>
            <td>45</td>
            <td>4D</td>
            <td>55</td>
            <td>5D</td>
            <td>65</td>
            <td>6D</td>
            <td>75</td>
            <td>7D</td>
        </tr>
        <tr>
            <td>[BP]+disp8</td>
            <td>SS</td>
            <td>110</td>
            <td>46</td>
            <td>4E</td>
            <td>56</td>
            <td>5E</td>
            <td>66</td>
            <td>6E</td>
            <td>76</td>
            <td>7E</td>
        </tr>
        <tr>
            <td>[BX]+disp8</td>
            <td>DS</td>
            <td>111</td>
            <td>47</td>
            <td>4F</td>
            <td>57</td>
            <td>5F</td>
            <td>67</td>
            <td>6F</td>
            <td>77</td>
            <td>7F</td>
        </tr>
        <tr class="section-start">
            <td>[BX+SI]+disp16</td>
            <td>DS</td>
            <td rowspan="8">10</td>
            <td>000</td>
            <td>80</td>
            <td>88</td>
            <td>90</td>
            <td>98</td>
            <td>A0</td>
            <td>A8</td>
            <td>B0</td>
            <td>B8</td>
        </tr>
        <tr>
            <td>[BX+DI]+disp16</td>
            <td>DS</td>
            <td>001</td>
            <td>81</td>
            <td>89</td>
            <td>91</td>
            <td>99</td>
            <td>A1</td>
            <td>A9</td>
            <td>B1</td>
            <td>B9</td>
        </tr>
        <tr>
            <td>[BP+SI]+disp16</td>
            <td>SS</td>
            <td>010</td>
            <td>82</td>
            <td>8A</td>
            <td>92</td>
            <td>9A</td>
            <td>A2</td>
            <td>AA</td>
            <td>B2</td>
            <td>BA</td>
        </tr>
        <tr>
            <td>[BP+DI]+disp16</td>
            <td>SS</td>
            <td>011</td>
            <td>83</td>
            <td>8B</td>
            <td>93</td>
            <td>9B</td>
            <td>A3</td>
            <td>AB</td>
            <td>B3</td>
            <td>BB</td>
        </tr>
        <tr>
            <td>[SI]+disp16</td>
            <td>DS</td>
            <td>100</td>
            <td>84</td>
            <td>8C</td>
            <td>94</td>
            <td>9C</td>
            <td>A4</td>
            <td>AC</td>
            <td>B4</td>
            <td>BC</td>
        </tr>
        <tr>
            <td>[DI]+disp16</td>
            <td>DS</td>
            <td>101</td>
            <td>85</td>
            <td>8D</td>
            <td>95</td>
            <td>9D</td>
            <td>A5</td>
            <td>AD</td>
            <td>B5</td>
            <td>BD</td>
        </tr>
        <tr>
            <td>[BP]+disp16</td>
            <td>SS</td>
            <td>110</td>
            <td>86</td>
            <td>8E</td>
            <td>96</td>
            <td>9E</td>
            <td>A6</td>
            <td>AE</td>
            <td>B6</td>
            <td>BE</td>
        </tr>
        <tr>
            <td>[BX]+disp16</td>
            <td>DS</td>
            <td>111</td>
            <td>87</td>
            <td>8F</td>
            <td>97</td>
            <td>9F</td>
            <td>A7</td>
            <td>AF</td>
            <td>B7</td>
            <td>BF</td>
        </tr>
        <tr class="section-start">
            <th class="addressing-mode" rowspan="8" scope="rowgroup"><span>Register Addressing Modes</span></th>
            <td>AX/AL</td>
            <td>&mdash;</td>
            <td rowspan="8">11</td>
            <td>000</td>
            <td>C0</td>
            <td>C8</td>
            <td>D0</td>
            <td>D8</td>
            <td>E0</td>
            <td>E8</td>
            <td>F0</td>
            <td>F8</td>
        </tr>
        <tr>
            <td>CX/CL</td>
            <td>&mdash;</td>
            <td>001</td>
            <td>C1</td>
            <td>C9</td>
            <td>D1</td>
            <td>D9</td>
            <td>E1</td>
            <td>E9</td>
            <td>F1</td>
            <td>F9</td>
        </tr>
        <tr>
            <td>DX/DL</td>
            <td>&mdash;</td>
            <td>010</td>
            <td>C2</td>
            <td>CA</td>
            <td>D2</td>
            <td>DA</td>
            <td>E2</td>
            <td>EA</td>
            <td>F2</td>
            <td>FA</td>
        </tr>
        <tr>
            <td>BX/BL</td>
            <td>&mdash;</td>
            <td>011</td>
            <td>C3</td>
            <td>CB</td>
            <td>D3</td>
            <td>DB</td>
            <td>E3</td>
            <td>EB</td>
            <td>F3</td>
            <td>FB</td>
        </tr>
        <tr>
            <td>SP/AH</td>
            <td>&mdash;</td>
            <td>100</td>
            <td>C4</td>
            <td>CC</td>
            <td>D4</td>
            <td>DC</td>
            <td>E4</td>
            <td>EC</td>
            <td>F4</td>
            <td>FC</td>
        </tr>
        <tr>
            <td>BP/CH</td>
            <td>&mdash;</td>
            <td>101</td>
            <td>C5</td>
            <td>CD</td>
            <td>D5</td>
            <td>DD</td>
            <td>E5</td>
            <td>ED</td>
            <td>F5</td>
            <td>FD</td>
        </tr>
        <tr>
            <td>SI/DH</td>
            <td>&mdash;</td>
            <td>110</td>
            <td>C6</td>
            <td>CE</td>
            <td>D6</td>
            <td>DE</td>
            <td>E6</td>
            <td>EE</td>
            <td>F6</td>
            <td>FE</td>
        </tr>
        <tr>
            <td>DI/BH</td>
            <td>&mdash;</td>
            <td>111</td>
            <td>C7</td>
            <td>CF</td>
            <td>D7</td>
            <td>DF</td>
            <td>E7</td>
            <td>EF</td>
            <td>F7</td>
            <td>FF</td>
        </tr>
    </tbody>
</table>
</div>

## 32-Bit ModR/M

<div class="table-wrapper">
<table class="modrm-table">
    <thead>
        <tr>
            <td colspan="5">r8</td>
            <td>AL</td><td>CL</td><td>DL</td><td>BL</td><td>AH</td><td>CH</td><td>DH</td><td>BH</td>
        </tr>
        <tr>
            <td colspan="5">r16</td>
            <td>AX</td><td>CX</td><td>DX</td><td>BX</td><td>SP</td><td>BP</td><td>SI</td><td>DI</td>
        </tr>
        <tr>
            <td colspan="5">r32</td>
            <td>EAX</td><td>ECX</td><td>EDX</td><td>EBX</td><td>ESP</td><td>EBP</td><td>ESI</td><td>EDI</td>
        </tr>
        <tr>
            <td colspan="5">Ext</td>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td>
        </tr>
        <tr>
            <td colspan="5">REG</td>
            <td>000</td><td>001</td><td>010</td><td>011</td><td>100</td><td>101</td><td>110</td><td>111</td>
        </tr>
        <tr class="section-start">
            <th aria-label="Addressing mode"></th>
            <th>Effective Address</th>
            <th>Base</th>
            <th>Mod</th>
            <th>R/M</th>
            <th colspan="8">Value of ModR/M Byte</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th class="addressing-mode" rowspan="24" scope="rowgroup"><span>Memory Addressing Modes</span></th>
            <td>[EAX]</td><td>DS</td><td rowspan="8">00</td><td>000</td>
            <td>00</td><td>08</td><td>10</td><td>18</td><td>20</td><td>28</td><td>30</td><td>38</td>
        </tr>
        <tr><td>[ECX]</td><td>DS</td><td>001</td><td>01</td><td>09</td><td>11</td><td>19</td><td>21</td><td>29</td><td>31</td><td>39</td></tr>
        <tr><td>[EDX]</td><td>DS</td><td>010</td><td>02</td><td>0A</td><td>12</td><td>1A</td><td>22</td><td>2A</td><td>32</td><td>3A</td></tr>
        <tr><td>[EBX]</td><td>DS</td><td>011</td><td>03</td><td>0B</td><td>13</td><td>1B</td><td>23</td><td>2B</td><td>33</td><td>3B</td></tr>
        <tr><td>[~SIB~]</td><td>DS/SS</td><td>100</td><td>04</td><td>0C</td><td>14</td><td>1C</td><td>24</td><td>2C</td><td>34</td><td>3C</td></tr>
        <tr><td>disp32</td><td>DS</td><td>101</td><td>05</td><td>0D</td><td>15</td><td>1D</td><td>25</td><td>2D</td><td>35</td><td>3D</td></tr>
        <tr><td>[ESI]</td><td>DS</td><td>110</td><td>06</td><td>0E</td><td>16</td><td>1E</td><td>26</td><td>2E</td><td>36</td><td>3E</td></tr>
        <tr><td>[EDI]</td><td>DS</td><td>111</td><td>07</td><td>0F</td><td>17</td><td>1F</td><td>27</td><td>2F</td><td>37</td><td>3F</td></tr>
        <tr class="section-start">
            <td>[EAX]+disp8</td><td>DS</td><td rowspan="8">01</td><td>000</td>
            <td>40</td><td>48</td><td>50</td><td>58</td><td>60</td><td>68</td><td>70</td><td>78</td>
        </tr>
        <tr><td>[ECX]+disp8</td><td>DS</td><td>001</td><td>41</td><td>49</td><td>51</td><td>59</td><td>61</td><td>69</td><td>71</td><td>79</td></tr>
        <tr><td>[EDX]+disp8</td><td>DS</td><td>010</td><td>42</td><td>4A</td><td>52</td><td>5A</td><td>62</td><td>6A</td><td>72</td><td>7A</td></tr>
        <tr><td>[EBX]+disp8</td><td>DS</td><td>011</td><td>43</td><td>4B</td><td>53</td><td>5B</td><td>63</td><td>6B</td><td>73</td><td>7B</td></tr>
        <tr><td>[~SIB~]+disp8</td><td>DS/SS</td><td>100</td><td>44</td><td>4C</td><td>54</td><td>5C</td><td>64</td><td>6C</td><td>74</td><td>7C</td></tr>
        <tr><td>[EBP]+disp8</td><td>SS</td><td>101</td><td>45</td><td>4D</td><td>55</td><td>5D</td><td>65</td><td>6D</td><td>75</td><td>7D</td></tr>
        <tr><td>[ESI]+disp8</td><td>DS</td><td>110</td><td>46</td><td>4E</td><td>56</td><td>5E</td><td>66</td><td>6E</td><td>76</td><td>7E</td></tr>
        <tr><td>[EDI]+disp8</td><td>DS</td><td>111</td><td>47</td><td>4F</td><td>57</td><td>5F</td><td>67</td><td>6F</td><td>77</td><td>7F</td></tr>
        <tr class="section-start">
            <td>[EAX]+disp32</td><td>DS</td><td rowspan="8">10</td><td>000</td>
            <td>80</td><td>88</td><td>90</td><td>98</td><td>A0</td><td>A8</td><td>B0</td><td>B8</td>
        </tr>
        <tr><td>[ECX]+disp32</td><td>DS</td><td>001</td><td>81</td><td>89</td><td>91</td><td>99</td><td>A1</td><td>A9</td><td>B1</td><td>B9</td></tr>
        <tr><td>[EDX]+disp32</td><td>DS</td><td>010</td><td>82</td><td>8A</td><td>92</td><td>9A</td><td>A2</td><td>AA</td><td>B2</td><td>BA</td></tr>
        <tr><td>[EBX]+disp32</td><td>DS</td><td>011</td><td>83</td><td>8B</td><td>93</td><td>9B</td><td>A3</td><td>AB</td><td>B3</td><td>BB</td></tr>
        <tr><td>[~SIB~]+disp32</td><td>DS/SS</td><td>100</td><td>84</td><td>8C</td><td>94</td><td>9C</td><td>A4</td><td>AC</td><td>B4</td><td>BC</td></tr>
        <tr><td>[EBP]+disp32</td><td>SS</td><td>101</td><td>85</td><td>8D</td><td>95</td><td>9D</td><td>A5</td><td>AD</td><td>B5</td><td>BD</td></tr>
        <tr><td>[ESI]+disp32</td><td>DS</td><td>110</td><td>86</td><td>8E</td><td>96</td><td>9E</td><td>A6</td><td>AE</td><td>B6</td><td>BE</td></tr>
        <tr><td>[EDI]+disp32</td><td>DS</td><td>111</td><td>87</td><td>8F</td><td>97</td><td>9F</td><td>A7</td><td>AF</td><td>B7</td><td>BF</td></tr>
        <tr class="section-start">
            <th class="addressing-mode" rowspan="8" scope="rowgroup"><span>Register Addressing Modes</span></th>
            <td>EAX/AX/AL</td><td>&mdash;</td><td rowspan="8">11</td><td>000</td>
            <td>C0</td><td>C8</td><td>D0</td><td>D8</td><td>E0</td><td>E8</td><td>F0</td><td>F8</td>
        </tr>
        <tr><td>ECX/CX/CL</td><td>&mdash;</td><td>001</td><td>C1</td><td>C9</td><td>D1</td><td>D9</td><td>E1</td><td>E9</td><td>F1</td><td>F9</td></tr>
        <tr><td>EDX/DX/DL</td><td>&mdash;</td><td>010</td><td>C2</td><td>CA</td><td>D2</td><td>DA</td><td>E2</td><td>EA</td><td>F2</td><td>FA</td></tr>
        <tr><td>EBX/BX/BL</td><td>&mdash;</td><td>011</td><td>C3</td><td>CB</td><td>D3</td><td>DB</td><td>E3</td><td>EB</td><td>F3</td><td>FB</td></tr>
        <tr><td>ESP/SP/AH</td><td>&mdash;</td><td>100</td><td>C4</td><td>CC</td><td>D4</td><td>DC</td><td>E4</td><td>EC</td><td>F4</td><td>FC</td></tr>
        <tr><td>EBP/BP/CH</td><td>&mdash;</td><td>101</td><td>C5</td><td>CD</td><td>D5</td><td>DD</td><td>E5</td><td>ED</td><td>F5</td><td>FD</td></tr>
        <tr><td>ESI/SI/DH</td><td>&mdash;</td><td>110</td><td>C6</td><td>CE</td><td>D6</td><td>DE</td><td>E6</td><td>EE</td><td>F6</td><td>FE</td></tr>
        <tr><td>EDI/DI/BH</td><td>&mdash;</td><td>111</td><td>C7</td><td>CF</td><td>D7</td><td>DF</td><td>E7</td><td>EF</td><td>F7</td><td>FF</td></tr>
    </tbody>
</table>
</div>

## SIB Byte

<div class="table-wrapper">
<table class="sib-table">
    <thead>
        <tr>
            <td colspan="3">r32</td>
            <td>EAX</td><td>ECX</td><td>EDX</td><td>EBX</td><td>ESP</td><td><a href="#sib-base-101-note">[--]<sup>*</sup></a></td><td>ESI</td><td>EDI</td>
        </tr>
        <tr>
            <td colspan="3">Base</td>
            <td>000</td><td>001</td><td>010</td><td>011</td><td>100</td><td>101</td><td>110</td><td>111</td>
        </tr>
        <tr class="section-start">
            <th>Effective Address</th>
            <th>SS</th>
            <th>Index</th>
            <th colspan="8">Value of SIB Byte</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>[EAX]</td><td rowspan="8">00</td><td>000</td><td>00</td><td>01</td><td>02</td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td></tr>
        <tr><td>[ECX]</td><td>001</td><td>08</td><td>09</td><td>0A</td><td>0B</td><td>0C</td><td>0D</td><td>0E</td><td>0F</td></tr>
        <tr><td>[EDX]</td><td>010</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td></tr>
        <tr><td>[EBX]</td><td>011</td><td>18</td><td>19</td><td>1A</td><td>1B</td><td>1C</td><td>1D</td><td>1E</td><td>1F</td></tr>
        <tr><td>None</td><td>100</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td></tr>
        <tr><td>[EBP]</td><td>101</td><td>28</td><td>29</td><td>2A</td><td>2B</td><td>2C</td><td>2D</td><td>2E</td><td>2F</td></tr>
        <tr><td>[ESI]</td><td>110</td><td>30</td><td>31</td><td>32</td><td>33</td><td>34</td><td>35</td><td>36</td><td>37</td></tr>
        <tr><td>[EDI]</td><td>111</td><td>38</td><td>39</td><td>3A</td><td>3B</td><td>3C</td><td>3D</td><td>3E</td><td>3F</td></tr>
        <tr class="section-start"><td>[EAX * 2]</td><td rowspan="8">01</td><td>000</td><td>40</td><td>41</td><td>42</td><td>43</td><td>44</td><td>45</td><td>46</td><td>47</td></tr>
        <tr><td>[ECX * 2]</td><td>001</td><td>48</td><td>49</td><td>4A</td><td>4B</td><td>4C</td><td>4D</td><td>4E</td><td>4F</td></tr>
        <tr><td>[EDX * 2]</td><td>010</td><td>50</td><td>51</td><td>52</td><td>53</td><td>54</td><td>55</td><td>56</td><td>57</td></tr>
        <tr><td>[EBX * 2]</td><td>011</td><td>58</td><td>59</td><td>5A</td><td>5B</td><td>5C</td><td>5D</td><td>5E</td><td>5F</td></tr>
        <tr><td><a href="#sib-no-index-note">None<sup>***</sup></a></td><td>100</td><td>60</td><td>61</td><td>62</td><td>63</td><td>64</td><td>65</td><td>66</td><td>67</td></tr>
        <tr><td>[EBP * 2]</td><td>101</td><td>68</td><td>69</td><td>6A</td><td>6B</td><td>6C</td><td>6D</td><td>6E</td><td>6F</td></tr>
        <tr><td>[ESI * 2]</td><td>110</td><td>70</td><td>71</td><td>72</td><td>73</td><td>74</td><td>75</td><td>76</td><td>77</td></tr>
        <tr><td>[EDI * 2]</td><td>111</td><td>78</td><td>79</td><td>7A</td><td>7B</td><td>7C</td><td>7D</td><td>7E</td><td>7F</td></tr>
        <tr class="section-start"><td>[EAX * 4]</td><td rowspan="8">10</td><td>000</td><td>80</td><td>81</td><td>82</td><td>83</td><td>84</td><td>85</td><td>86</td><td>87</td></tr>
        <tr><td>[ECX * 4]</td><td>001</td><td>88</td><td>89</td><td>8A</td><td>8B</td><td>8C</td><td>8D</td><td>8E</td><td>8F</td></tr>
        <tr><td>[EDX * 4]</td><td>010</td><td>90</td><td>91</td><td>92</td><td>93</td><td>94</td><td>95</td><td>96</td><td>97</td></tr>
        <tr><td>[EBX * 4]</td><td>011</td><td>98</td><td>99</td><td>9A</td><td>9B</td><td>9C</td><td>9D</td><td>9E</td><td>9F</td></tr>
        <tr><td><a href="#sib-no-index-note">None<sup>***</sup></a></td><td>100</td><td>A0</td><td>A1</td><td>A2</td><td>A3</td><td>A4</td><td>A5</td><td>A6</td><td>A7</td></tr>
        <tr><td>[EBP * 4]</td><td>101</td><td>A8</td><td>A9</td><td>AA</td><td>AB</td><td>AC</td><td>AD</td><td>AE</td><td>AF</td></tr>
        <tr><td>[ESI * 4]</td><td>110</td><td>B0</td><td>B1</td><td>B2</td><td>B3</td><td>B4</td><td>B5</td><td>B6</td><td>B7</td></tr>
        <tr><td>[EDI * 4]</td><td>111</td><td>B8</td><td>B9</td><td>BA</td><td>BB</td><td>BC</td><td>BD</td><td>BE</td><td>BF</td></tr>
        <tr class="section-start"><td>[EAX * 8]</td><td rowspan="8">11</td><td>000</td><td>C0</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td></tr>
        <tr><td>[ECX * 8]</td><td>001</td><td>C8</td><td>C9</td><td>CA</td><td>CB</td><td>CC</td><td>CD</td><td>CE</td><td>CF</td></tr>
        <tr><td>[EDX * 8]</td><td>010</td><td>D0</td><td>D1</td><td>D2</td><td>D3</td><td>D4</td><td>D5</td><td>D6</td><td>D7</td></tr>
        <tr><td>[EBX * 8]</td><td>011</td><td>D8</td><td>D9</td><td>DA</td><td>DB</td><td>DC</td><td>DD</td><td>DE</td><td>DF</td></tr>
        <tr><td><a href="#sib-no-index-note">None<sup>***</sup></a></td><td>100</td><td>E0</td><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E5</td><td>E6</td><td>E7</td></tr>
        <tr><td>[EBP * 8]</td><td>101</td><td>E8</td><td>E9</td><td>EA</td><td>EB</td><td>EC</td><td>ED</td><td>EE</td><td>EF</td></tr>
        <tr><td>[ESI * 8]</td><td>110</td><td>F0</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td><td>F6</td><td>F7</td></tr>
        <tr><td>[EDI * 8]</td><td>111</td><td>F8</td><td>F9</td><td>FA</td><td>FB</td><td>FC</td><td>FD</td><td>FE</td><td>FF</td></tr>
    </tbody>
</table>
</div>

<a id="sib-base-101-note"></a>

> [!NOTE]
> *When `Base` is `101`, compute the base and index using the EBP Slot Table below.

### EBP Slot Table

| Mod | Base |   | Scaled Index | Disp |
|:---:|:----:|:-:|:------------:|:----:|
| `00` | &mdash; | &mdash; | [Scaled Index] | `disp32` |
| `01` | EBP | + | [Scaled Index] | `disp8` |
| `10` | EBP | + | [Scaled Index] | `disp32` |
| <a href="#sib-mod-11-note"><code>11</code><sup>**</sup></a> | &mdash; | &mdash; | &mdash; | &mdash; |

<a id="sib-mod-11-note"></a>

> [!NOTE]
> **A `Mod` value of `11` in the EBP slot table is impossible because it would not have indicated a SIB byte.

<a id="sib-no-index-note"></a>

> [!NOTE]
> ***When the `Index` field is `100`, indicating no index register, the `SS` field must be `00`. If `Index` is `100` and `SS` is not `00`, the effective address is undefined.
