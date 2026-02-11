import { useState } from "react";

const Header = ({ dark, setDark }) => {
  const [menu, setMenu] = useState(false);

  return (
    <header className="header">
      <h2 className="logo">Harsh</h2>

      <div className="actions">
        <button onClick={() => setDark(!dark)} className="theme-btn">
          {dark ? "☀️" : "🌙"}
        </button>

        <button className="menu-btn" onClick={() => setMenu(!menu)}>
          ☰
        </button>
      </div>

      <nav className={menu ? "nav active" : "nav"}>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>
  );
};

export default Header;
