import React from "react";
import logoClubTenisVdM from "../../img/logo.png";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-primary">
			<div className="container-fluid">
				<Link to="/">
				<img src={logoClubTenisVdM} width={100} height={100} />
				</Link>
				<Link to="/registro">
				<p className="text-light">Navbar</p>
				</Link>
				<Link to="/">
				<p className="text-light">Navbar</p>
				</Link>
				<Link to="/">
				<p className="text-light">Navbar</p>
				</Link>
				<Link to="/">
				<p className="text-light">Navbar</p>
				</Link>
    
    
			</div>
		</nav>
	);
};
