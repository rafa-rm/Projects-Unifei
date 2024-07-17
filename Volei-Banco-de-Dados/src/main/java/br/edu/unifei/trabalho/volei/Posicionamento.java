package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public abstract class Posicionamento implements Serializable{
	private static final long serialVersionUID = 2291849873389612237L;
	@Id
	@GeneratedValue
	private int codigo;
	@Enumerated(EnumType.STRING)
	private RotacaoEnum posicaoRotacao;
	public abstract void realizaAcao();
}
