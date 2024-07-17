package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class Torcida implements Serializable{
	private static final long serialVersionUID = 4211943959809625328L;
	@Id
	private String nome;
	private int quantidade;
	private float animacao;
	private String grito;
	@OneToOne
	private Equipe equipe;
}