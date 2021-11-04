import React, { useEffect, useState } from 'react';
import "../css/search_page.css"
import DualSlider from './dual_range_slider'


export default function SearchPage ()
{
    const [adv_search, setAdv_search] = useState(false)
    useEffect(() => console.log(adv_search), [adv_search])

    {/* TODO: Look into how to use form elements and make this a form */}
    return (
        <div className="search_container">
            <button id="Random_button">按此隨機搜尋好課</button>
            <div className="search_bar">
                <input id="searchform" placeholder="🔍搜尋"/>
                <button id="submit_button" type="submit" form="searchform">➜</button>
            </div>
            {/* TODO: coloring the elements */}
            <button id="advanced_option" onClick={()=>setAdv_search(!adv_search)}>▼ Advanced Options</button>
            {
                adv_search ?
                <div className="advanced_condition">
                    <div className="platform_option">
                        <p>平台</p>
                        {
                            ["Hahow", "TibaMe", "Yotta", "PressPlay"].map((text, index) =>{
                                return <Checkboxitem id={`platform_option${index}`} text={text} />
                            })
                        }
                    </div>
                    <div className="category_option">
                        <p>主題</p>
                        {
                            ["語言", "藝術", "設計", "多媒體設計", "程式", "行銷", "投資理財", "職場技能", "生活品味"].map((text, index) =>{
                                return <Checkboxitem id={`category_option${index}`} text={text} />
                            })
                        }
                    </div>
                    <div className="price">
                        <p>價格</p> <br/>
                        {/* FIXME The slider's first input is tranparent */}
                        {/* REVIEW Is it a big deal though */}
                        <DualSlider min={0} max={10000} step={1000}/>
                    </div>
                    <br/>
                    <div className="fundraise">
                        <p>類型</p>
                        <Checkboxitem id="fundraise1" text="募資/預售"/>
                        <Checkboxitem id="fundraise2" text="已上架課程"/>
                    </div>
                    <div className="course_length">
                        <p>課程時長</p>
                        <DualSlider min={0} max={24} step={2}/>
                    </div>
                    <div className="student_num">
                        <p>學生總人數</p>
                        <DualSlider min={0} max={1000} step={50}/>
                    </div>
                    <div className="discount">
                        <p>折扣</p>
                        <Checkboxitem id="discount1" text="有"/>
                    </div>
                </div> : ""
            }
        </div>
    )
}

function Checkboxitem ({id, text})
{
    return (
    <>
        <input type="checkbox" id={id} />
        <label for={id}>{text}</label>
    </>
    )
} 
