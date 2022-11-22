import styles from "./Header.module.css";

const Header = (props) => {
  const { className } = props;

  return (
    <div className={`${className} ${styles.Main}`}>
      <h1 className={styles.Title}>FAVITES-Lite <span className={styles.AltText}>Config Designer</span></h1>
    </div>
  );
};

export default Header;
