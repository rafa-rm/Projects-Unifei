package br.edu.unifei.trabalho.volei;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;

import lombok.Data;

@Data
@Entity
public class Ponto implements Serializable{
	private static final long serialVersionUID = -4410425559949271080L;
	@Id
	@GeneratedValue
	private int codigo;
	private int duracaoSegundos;
	private boolean disputado;
	@ManyToOne
	private Equipe equipe;
	@ManyToOne
	private SetDisputado set;
	@OneToMany
	private List<Jogada> jogadas = new ArrayList<Jogada>();
}