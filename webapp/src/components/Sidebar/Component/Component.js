import styles from "./Component.module.css";
import { useSelector, useDispatch } from "react-redux";

const Component = (props) => {
  const { name, onClick, className } = props;
  const config = useSelector((state) => state.config.value);
  
  return (
    <div className={`${className} ${styles.Main} ${config[name] && styles.InProgress}`} onClick={onClick}>
      <h4>{name}</h4>
      {name in config ?
        <span>{config[name]["model"]}</span> :
        <span>Not Selected</span>
      }
    </div>
  );
};

export default Component;
