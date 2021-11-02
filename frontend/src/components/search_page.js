import React, { useEffect, useState } from 'react';
import "../css/search_page.css"

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
                <button type="submit" form="searchform">➜</button>
            </div>
            {/* TODO: Find a way to organize this. It looks ugly as hell now */}
            <button id="advanced_option" onClick={()=>setAdv_search(!adv_search)}>▼ Advanced Options</button>
            {
                adv_search ?
                <div className="advanced_condition">
                    <div className="platform_option">
                        <p>平台</p>
                        {
                            ["Hahow", "TibaMe", "Yotta", "PressPlay"].map((text, index) =>{
                                return <Checkbox_item id={`platform_option${index}`} text={text} />
                            })
                        }
                    </div>
                    <div className="category_option">
                        <p>主題</p>
                        {
                            ["語言", "藝術", "設計", "多媒體設計", "程式", "行銷", "投資理財", "職場技能", "生活品味"].map((text, index) =>{
                                return <Checkbox_item id={`category_option${index}`} text={text} />
                            })
                        }
                    </div>
                    <div className="price">
                        <p>價格</p>
                    </div>
                    <div className="fundraise">
                        <p>類型</p>
                        <Checkbox_item id="fundraise1" text="募資/預售"/>
                        <Checkbox_item id="fundraise2" text="已上架課程"/>
                    </div>
                    <div className="course_length">
                        <p>課程時長</p>
                    </div>
                    <div className="student_num">
                        <p>學生總人數</p>
                    </div>
                    <div className="discount">
                        <p>折扣</p>
                        <Checkbox_item id="discount1" text="有"/>
                    </div>
                </div> : ""
            }
        </div>
    )
}

function Checkbox_item ({id, text})
{
    return (
    <>
        <input type="checkbox" id={id} />
        <label for={id}>{text}</label>
    </>
    )
} 

// TODO: implement this https://www.youtube.com/watch?v=DfSYmk_6vk8&ab_channel=CodingArtist
function Double_range_slider ()
{
    
}