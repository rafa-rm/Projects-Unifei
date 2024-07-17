package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

import lombok.Data;

@Data
@Entity
public class Jogada implements Serializable{
	private static final long serialVersionUID = 8412532875680108545L;
	@Id
	@GeneratedValue
	private int codigo;
	@Enumerated(EnumType.STRING)
	private FundamentoEnum fundamento;
	private int tempo;
	@ManyToOne
	private Jogador jogador;
}
