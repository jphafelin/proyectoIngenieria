import React from "react";
import "../../styles/ContactUs.css";

const ContactUs = () => {
    return (
        <div className="contact-body">
            <div className="singup-container" id="container">
                <div className="singup-form-container singup-sign-up">
                    <form>
                        <h1>Create Account</h1>
                        <div className="singup-social-icons">
                            <a href="#" className="icon"><i className="fa-brands fa-google-plus-g"></i></a>
                            <a href="#" className="icon"><i className="fa-brands fa-facebook-f"></i></a>
                            <a href="#" className="icon"><i className="fa-brands fa-github"></i></a>
                            <a href="#" className="icon"><i className="fa-brands fa-linkedin-in"></i></a>
                        </div>
                        <span>or use your email for registration</span>
                        <input type="text" placeholder="Name" />
                        <input type="email" placeholder="Email" />
                        <input type="password" placeholder="Password" />
                        <button type="submit">Sign Up</button>
                    </form>
                </div>
                <div className="singup-form-container singup-sign-in">
                    <form>
                        <h1>Sign In</h1>
                        <span>Use your email and password</span>
                        <input type="email" placeholder="Email" />
                        <input type="password" placeholder="Password" />
                        <a href="#">Forget Your Password?</a>
                        <button type="submit">Sign In</button>
                    </form>
                </div>
                <div className="singup-toggle-container">
                    <div className="singup-toggle">
                        <div className="singup-toggle-panel singup-toggle-left">
                            <h1>Welcome Back!</h1>
                            <p>Enter your personal details to use all of site features</p>
                            <button className="singup-hidden" id="login">Sign In</button>
                        </div>
                        <div className="singup-toggle-panel singup-toggle-right">
                            <h1>Hello, Friend!</h1>
                            <p>Register with your personal details to use all of site features</p>
                            <button className="singup-hidden" id="register">Sign Up</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ContactUs;