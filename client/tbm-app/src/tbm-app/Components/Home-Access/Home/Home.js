import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="home-page">
      <h1>Welcome to The Blessing Machine</h1>
      <p>A groundbreaking non-profit donation platform, tailored specifically for Christian organizations, aimed at revolutionizing the way they raise and manage funds.</p>
      <Link to="/dashboard" className="btn">Get Started</Link>
    </div>
  );
};

export default HomePage;
