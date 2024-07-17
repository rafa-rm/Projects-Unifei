package br.edu.unifei.trabalho.volei;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
@Entity
public class Arbitro extends Pessoa implements Serializable{
	private static final long serialVersionUID = 1670132557220186796L;
	@Enumerated(EnumType.STRING)
	private LadoEnum decisaoPonto;
	private int pontuacaoEquipe1;
	private int pontuacaoEquipe2;
	@OneToOne
	private Partida partida;
	@OneToMany
	private List<Regra> regras = new ArrayList<Regra>();
	@OneToOne
	private Ponto ponto;
	
}