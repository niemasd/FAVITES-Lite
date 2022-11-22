import React from "react";
import Component from "./Component/Component";
import styles from "./Sidebar.module.css";

const Sidebar = (props) => {
  const { className } = props;

  const li = [
    "Contact Network",
    "Transmission Network",
    "Sample Times",
    "Viral Phylogeny (Transmissions)",
    "Viral Phylogeny (Seeds)",
  ];

  return (
    <div className={className}>
      {li.map((name) => (
        <Component key={name} name={name} />
      ))}
    </div>
  );
};

export default Sidebar;
