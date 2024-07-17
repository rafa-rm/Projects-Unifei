package br.edu.unifei.trabalho.volei;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class Torneio implements Serializable{
	private static final long serialVersionUID = -1659057523764766993L;
	@Id
	private String nome;
	private float premiacao;
	private String organizador;
	@OneToOne
	private Equipe ganhador;
	@OneToMany
	private List<Partida> partidas = new ArrayList<Partida>();
}
