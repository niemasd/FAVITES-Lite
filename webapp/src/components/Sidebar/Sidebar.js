import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSelected } from "../../features/selected/selectedSlice";
import Component from "./Component/Component";
import styles from "./Sidebar.module.css";
import globalJSON from "../../files/global.json";

const Sidebar = (props) => {
  const { className } = props;
  const { CONFIG_KEYS } = globalJSON;
  
  const selected = useSelector((state) => state.selected.value);
  const dispatch = useDispatch();

  return (
    <div className={`${className} ${styles.Main}`}>
      {CONFIG_KEYS.map((name) => (
        <Component
          key={name}
          name={name}
          className={name === selected ? styles.SelectedComponent : ""}
          onClick={() => dispatch(setSelected(name))}
        />
      ))}
    </div>
  );
};

export default Sidebar;
