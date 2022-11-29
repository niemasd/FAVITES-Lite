import styles from "./Component.module.css";
import { useSelector, useDispatch } from "react-redux";
import globalJSON from "../../../files/global.json";

const Component = (props) => {
  const { name, onClick, className } = props;
  const config = useSelector((state) => state.config.value);

  /**
   * Sets color of sidebar component based on if user picked a model and filled out all parameters
   * @param {*} name name of sidebar option (e.g. Contact Network, Transmission Network) 
   * @returns style
   */
  const setColor = (name) => {
    // If name is in config (i.e. user has chosen a model for the name)
    if (config[name]) {
      let totalParams = globalJSON.MODELS[name][config[name]["model"]].PARAM;
      let totalParamCount = Object.keys(totalParams).length;
      
      // If user has specified values for model's params, compare number of completed params to total params
      if (config[name]["param"]) {
        let completedParamCount = Object.keys(config[name]["param"]).length;
        if (completedParamCount == totalParamCount) {
          return styles.Done;
        }
        return styles.InProgress;
      }

      // If there are no params to choose from, return styles.Done
      if (totalParamCount === 0) {
        return styles.Done;
      }
      return styles.InProgress;
    }
    return styles.NotStarted;
  }
  
  return (
    <div className={`${className} ${styles.Main} ${setColor(name)}`} onClick={onClick}>
      <h4>{name}</h4>
      {name in config ?
        <span>{config[name]["model"]}</span> :
        <span>Not Selected</span>
      }
    </div>
  );
};

export default Component;
