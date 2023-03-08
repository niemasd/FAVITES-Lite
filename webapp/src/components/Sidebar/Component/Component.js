import styles from "./Component.module.css";
import { useSelector } from "react-redux";
import { status } from "../../../utils/utils";

const Component = (props) => {
  const { name, onClick, className } = props;
  const config = useSelector((state) => state.config.value);
  const statuses = useSelector((state) => state.statuses.value);

  const setColor = (name) => {
    if (!statuses[name]) {
      return styles.NotStarted;
    } else if (statuses[name] === status.INCOMPLETE) {
      return styles.InProgress;
    } else if (statuses[name] === status.COMPLETE) {
      return styles.Done;
    } else {
      return styles.Error;
    }
  };

  return (
    <div
      className={`${className} ${styles.Main} ${setColor(name)}`}
      onClick={onClick}
    >
      <h4>{name}</h4>
      {name in config ? (
        <span>{config[name]["model"]}</span>
      ) : (
        <span>Not Selected</span>
      )}
    </div>
  );
};

export default Component;
