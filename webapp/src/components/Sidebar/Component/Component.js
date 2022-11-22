import styles from "./Component.module.css";

const Component = (props) => {
  const { name } = props;

  return (
    <div className={styles.Main}>
      <h4>{name}</h4>
      <span>Not Selected</span>
    </div>
  );
};

export default Component;
