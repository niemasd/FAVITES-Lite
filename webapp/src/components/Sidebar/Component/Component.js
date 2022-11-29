import styles from "./Component.module.css";
import { useSelector, useDispatch } from "react-redux";
// import { setConfig } from "../../../features/config/configSlice";

const Component = (props) => {
  const { name, onClick, className } = props;
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  // console.log(config);
  // console.log(selected);
  
  return (
    <div className={`${className} ${styles.Main}`} onClick={onClick}>
      <h4>{name}</h4>
      {
        name in config ?
        <span>{config[name]["model"]}</span> :
        <span>Not Selected</span>
      }
    </div>
  );
};

export default Component;
