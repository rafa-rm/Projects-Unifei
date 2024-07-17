package br.edu.unifei.trabalho.volei;

import javax.persistence.Entity;
import javax.persistence.OneToOne;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
@Entity
public class Treinador extends Pessoa{
	private static final long serialVersionUID = -9020760181548496731L;
	private int tempoProfissao;
	private boolean exJogador;
	@OneToOne
	private Equipe equipe;
}
