import React from "react";
import Header from "../Header/Header";
import Sidebar from "../Sidebar/Sidebar";
import Body from "../Body/Body";
import styles from "./Layout.module.css";
import globalJSON from '../../files/global.json'

const Layout = () => {
  console.log(globalJSON)

  return (
      <div className={styles.Main}>
        <Header className={styles.Header} />
        <Sidebar className={styles.Sidebar} />
        <Body className={styles.Body} />
      </div>
  );
};

export default Layout;
