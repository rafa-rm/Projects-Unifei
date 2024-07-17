package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class Regra implements Serializable{
	private static final long serialVersionUID = -2816108932551483969L;
	@Id
	private String descricao;
	private String acaoTomada;
}
