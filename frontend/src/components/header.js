import React from 'react';
import {NodeExpandOutlined} from '@ant-design/icons'
import "../css/header.css"

export default function Header() {
    return (
        <>
            <NodeExpandOutlined />
            <h1>Online Course Finder</h1>
            <p>搜尋</p>
            <p>關於我們</p>
        </>
    )
}