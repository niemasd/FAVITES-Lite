import React, { useState } from "react";
import Header from "../Header/Header";
import Sidebar from "../Sidebar/Sidebar";
import Body from "../Body/Body";
import styles from "./Layout.module.css";

export const ConfigContext = React.createContext();

const Layout = () => {
  return (
    <ConfigContext.Provider value={{}}>
      <div className={styles.Main}>
        <Header className={styles.Header} />
        <Sidebar className={styles.Sidebar} />
        <Body className={styles.Body} />
      </div>
    </ConfigContext.Provider>
  );
};

export default Layout;
