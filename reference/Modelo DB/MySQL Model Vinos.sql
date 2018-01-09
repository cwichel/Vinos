-- MySQL Script generated by MySQL Workbench
-- vie 01 dic 2017 17:36:28 CLST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema vinosdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema vinosdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vinosdb` DEFAULT CHARACTER SET latin5 ;
USE `vinosdb` ;

-- -----------------------------------------------------
-- Table `vinosdb`.`estanques`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`estanques` (
  `id_estanque` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `numero` INT UNSIGNED NOT NULL,
  `descripcion` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id_estanque`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vinosdb`.`vinos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`vinos` (
  `id_vino` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NOT NULL,
  `tipo` VARCHAR(50) NOT NULL,
  `vina` VARCHAR(50) NOT NULL,
  `valle` VARCHAR(50) NOT NULL,
  `ano` SMALLINT NOT NULL,
  `descripcion` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id_vino`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vinosdb`.`espectros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`espectros` (
  `id_espectro` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `espectro` LONGBLOB NOT NULL,
  `flag_procesado` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_espectro`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vinosdb`.`fechas_espectros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`fechas_espectros` (
  `id_fecha_esp` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_vinos` INT UNSIGNED NOT NULL,
  `id_estanques` INT UNSIGNED NOT NULL,
  `id_espectros` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_fecha_esp`, `id_vinos`, `id_estanques`, `id_espectros`),
  INDEX `fk_Fechas_Vinos1_idx` (`id_vinos` ASC),
  INDEX `fk_Fechas_Estanques1_idx` (`id_estanques` ASC),
  INDEX `fk_Fechas_Espectros1_idx` (`id_espectros` ASC),
  CONSTRAINT `fk_Fechas_Vinos1`
    FOREIGN KEY (`id_vinos`)
    REFERENCES `vinosdb`.`vinos` (`id_vino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fechas_Estanques1`
    FOREIGN KEY (`id_estanques`)
    REFERENCES `vinosdb`.`estanques` (`id_estanque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fechas_Espectros1`
    FOREIGN KEY (`id_espectros`)
    REFERENCES `vinosdb`.`espectros` (`id_espectro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vinosdb`.`parametros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`parametros` (
  `id_parametro` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `SO2L` FLOAT NOT NULL,
  `SO2T` FLOAT NOT NULL,
  `AV` FLOAT NOT NULL,
  `AT(Sulfurica)` FLOAT NOT NULL,
  `AT(Tartarica)` FLOAT NOT NULL,
  `PH` FLOAT NOT NULL,
  `MR` FLOAT NOT NULL,
  `GA` FLOAT NOT NULL,
  `Densidad` FLOAT NOT NULL,
  `id_espectros` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_parametro`, `id_espectros`),
  INDEX `fk_Parametros_Espectros1_idx` (`id_espectros` ASC),
  CONSTRAINT `fk_Parametros_Espectros1`
    FOREIGN KEY (`id_espectros`)
    REFERENCES `vinosdb`.`espectros` (`id_espectro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vinosdb`.`fechas_vinos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vinosdb`.`fechas_vinos` (
  `id_fecha_vin` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `fecha` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_estanques` INT UNSIGNED NOT NULL,
  `id_vinos` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_fecha_vin`, `id_estanques`, `id_vinos`),
  INDEX `fk_Fechas_Vinos_Estanques1_idx` (`id_estanques` ASC),
  INDEX `fk_Fechas_Vinos_Vinos1_idx` (`id_vinos` ASC),
  CONSTRAINT `fk_Fechas_Vinos_Estanques1`
    FOREIGN KEY (`id_estanques`)
    REFERENCES `vinosdb`.`estanques` (`id_estanque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fechas_Vinos_Vinos1`
    FOREIGN KEY (`id_vinos`)
    REFERENCES `vinosdb`.`vinos` (`id_vino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
