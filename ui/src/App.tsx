import React from 'react';
import 'antd/dist/antd.css';
import GlobalStyles from './styles/GlobalStyles';
import HomeView from "./views/HomeView";

function App() {
  return (
    <>
      <GlobalStyles/>
      <HomeView/>
    </>
  );
}

export default App;
