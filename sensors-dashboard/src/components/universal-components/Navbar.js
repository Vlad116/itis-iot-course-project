import React from 'react'
import { NavLink } from 'react-router-dom'

const Navbar = () => {
    return (
        <div className='navbar'>
            <NavLink exact to="/lighting" className='nav-item' activeClassName='nav-item-active'>
                <span>Забронировать</span>
            </NavLink>

            <NavLink exact to="/ambient" className='nav-item' activeClassName='nav-item-active'>
                <span>Сдать</span>
            </NavLink>

            <NavLink exact to="/about" className='nav-item' activeClassName='nav-item-active'>
                <span>Профиль</span>
            </NavLink>
        </div>
    )
}

export default Navbar