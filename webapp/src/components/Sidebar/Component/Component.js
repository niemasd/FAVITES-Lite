import styles from "./Component.module.css";
import { useSelector, useDispatch } from "react-redux";
import globalJSON from "../../../files/global.json";

const Component = (props) => {
  const { name, onClick, className } = props;
  const config = useSelector((state) => state.config.value);

  const setColor = (name) => {
    if (config[name]) {
      let totalParams = globalJSON.MODELS[name][config[name]["model"]].PARAM;
      let totalParamCount = Object.keys(totalParams).length;
      if (config[name]["param"]) {
        let completedParamCount = Object.keys(config[name]["param"]).length;

        if (completedParamCount == totalParamCount) {
          return styles.Done;
        }
        return styles.InProgress;
      }
      if (totalParamCount === 0) {
        return styles.Done;
      }
      return styles.InProgress;
    }
    return styles.Main;
  }
  
  return (
    <div className={`
      ${className}
      ${styles.Main}
      ${setColor(name)}
      `} 
      onClick={onClick}>
      <h4>{name}</h4>
      {name in config ?
        <span>{config[name]["model"]}</span> :
        <span>Not Selected</span>
      }
    </div>
  );
};

export default Component;
