import React, { useState } from "react";
import '../css/dual_range_slider.css'

export default function MultiRangeSlider ({min, max, step})
{
    const [value1, setValue1] = useState(max*0.3)
    const [value2, setValue2] = useState(max*0.7)

    return (
        <div className="dual_slider">
            <input type="range" min={min} max={max} value={value1} onChange={(e) => setValue1(e.target.value)} id="lower" step={step}/>
            <input type="range" min={min} max={max} value={value2} onChange={(e) => setValue2(e.target.value)} id="upper" step={step}/>
        </div>
      );
};