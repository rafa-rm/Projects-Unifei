package br.edu.unifei.trabalho.volei;

import java.awt.Color;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class Equipe implements Serializable{
	private static final long serialVersionUID = -5443138035582977430L;
	@Id
	private String nome;
	private String localidade;
	private Color corCamisa;
	@Enumerated(EnumType.STRING)
	private LadoEnum lado;
	@OneToOne
	private Torcida torcida;
	@OneToOne
	private Treinador treinador;
	@OneToMany
	private List<Jogador> jogadores= new ArrayList<Jogador>();
	@OneToMany
	private List<Ponto> pontos = new ArrayList<Ponto>();

}
